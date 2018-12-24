from django.utils.timezone import now
from . import models


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

        self.status_waiting = models.OrderStatus.objects.get(name="Ожидает исполнителя")
        self.status_in_process = models.OrderStatus.objects.get(name="В процессе")
        self.status_done = models.OrderStatus.objects.get(name="Выполнено")

    @staticmethod
    def load_workers():
        """
        Загружает работников
        :return: словарь в котором ключ - id работника,
        значение - объект класса Order (по умолчанию None)
        """
        user_id = models.MedWorkerProfile.objects.values_list('user_id', flat=True)
        orders = [None] * len(user_id)
        return dict(zip(user_id, orders))

    @staticmethod
    def load_orders():
        """
        Загружает незакрытые заявки, необходимо при восстановлении
        аварийно прерванной работы приложения
        :return: лист с объектами класса Order
        """
        not_done = list(models.OrderStatus.objects.all().filter(done=False))
        to_do = models.Order.objects.all().filter(status__in=not_done)
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
        if models.MedWorkerProfile.objects.filter(user_id=worker_id).exists():
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

    def find_free_worker(self):
        for worker in self.workers.keys():
            if self.is_worker_free(worker):
                return worker

        return None

    def pass_order_to_worker(self, worker_id, order_obj):
        if self.is_worker_free(worker_id):
            self.workers[worker_id] = order_obj

    def add_order(self, user_id, service_id):
        """
        Добовляет заявку в лист заявок
        :param user_id: id потребителя услуг (пациента)
        :param service_id: id оказываемой потребителю услуги
        """
        order = models.Order()
        order.user = user_id
        order.service = models.Service.objects.get(id=service_id)
        order.status = self.status_waiting
        order.save()

        worker = self.find_free_worker()
        if worker:
            self.pass_order_to_worker(worker, order)
        else:
            self.to_do.append(order)

    def open(self, worker_id):
        """
        Открывает заявку на обслуживание, меняя статус на соотвествующий
        :param worker_id: id пользователя, имеющего роль работника
        """
        order = self.workers[worker_id]
        order.status = self.status_in_process
        order.opening_date = now()
        order.save()

        self.workers[worker_id] = order

    def close(self, worker_id, report):
        """
        Закрывает заявку, меняет статус на соотвествующий, открепляет работника.
        Если есть невыполненные заявки, прекрепляет верхнюю к рабонику.
        :param worker_id: id пользователя, имеющего роль работника
        :param report: отчет о проделанной работе
        """
        order = self.workers[worker_id]
        self.workers[worker_id] = None

        order.status = self.status_done
        order.closing_date = now()
        order.report = report
        order.save()

        if len(self.to_do) > 0:
            order = self.to_do.pop(0)
            self.pass_order_to_worker(worker_id, order)