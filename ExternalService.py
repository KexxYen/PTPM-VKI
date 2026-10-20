import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class ExternalService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class FakeExternalService(ExternalService):
    def send(self, message):
        print(f"[Имитация отправки] {message}")
        logger.info("Имитация отправки выполнена успешно")
