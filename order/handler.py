from django.utils.timezone import now

from .models import OrderStatus, Order
from med_worker.models import MedWorkerProfile


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class OrderDistributor(metaclass=Singleton):
    """
    Этот класс описывает систему распределения заявок от потребителей услуг (пациентов)
    """
    def __init__(self):
        self.workers = self.load_workers()
        self.to_do = self.load_orders()

        self.status_waiting = OrderStatus.objects.get(name="Ожидает исполнителя")
        self.status_in_process = OrderStatus.objects.get(name="В процессе")
        self.status_done = OrderStatus.objects.get(name="Выполнено")

    @staticmethod
    def load_workers():
        """
        Загружает работников
        :return: словарь в котором ключ - id работника,
        значение - объект класса Order (по умолчанию None)
        """
        user_id = MedWorkerProfile.objects.values_list('user_id', flat=True)
        orders = [None] * len(user_id)
        return dict(zip(user_id, orders))

    @staticmethod
    def load_orders():
        """
        Загружает незакрытые заявки, необходимо при восстановлении
        аварийно прерванной работы приложения
        :return: лист с объектами класса Order
        """
        not_done = list(OrderStatus.objects.all().filter(done=False))
        to_do = Order.objects.all().filter(status__in=not_done)
        return list(to_do)

    def get_order_list(self):
        """
        :return: текущий лист с объектами класса Order
        """
        return self.to_do

    def add_worker(self, worker_id):
        """
        Добавляет в workers новый worker_id
        :param worker_id: id пользователя приложения, имеющего роль работника
        """
        if MedWorkerProfile.objects.filter(user_id=worker_id).exists():
            self.workers.update({worker_id: None})

    def is_worker_free(self, worker_id):
        """
        Проверяет, занят ли заявкой работник
        :param worker_id: id пользователя, имеющего роль работника
        :return: False если словарь workers по worker_id(ключ) содержит объект класса Order,
        иначе True
        """
        if self.workers[worker_id]:
            return False
        return True

    def add_order(self, user_id, service_id):
        """
        Добовляет заявку в лист заявок
        :param user_id: id потребителя услуг (пациента)
        :param service_id: id оказываемой потребителю услуги
        """
        order = Order()
        order.user = user_id
        order.service = service_id
        order.status = self.status_waiting
        order.save()

        self.to_do.append(order)

    def open(self, worker_id, to_do_number):
        """
        Открывает заявку на обслуживание, меняет статус на соотвествующий,
        закрепляет за ней работника.
        :param worker_id: id пользователя, имеющего роль работника
        :param to_do_number: номер заявки
        """
        order = self.to_do.pop(to_do_number)
        order.status = self.status_in_process
        order.opening_date = now()
        order.save()

        self.workers[worker_id] = order

    def close(self, worker_id, report):
        """
        Закрывает заявку, меняет статус на соотвествующий, открепляет работника.
        :param worker_id: id пользователя, имеющего роль работника
        :param report: отчет о проделанной работе
        """
        order = self.workers[worker_id]
        order.status = self.status_done
        order.closing_date = now()
        order.report = report
        order.save()

        self.workers[worker_id] = None
