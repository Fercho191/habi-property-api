from abc import ABC, abstractmethod

from core.shared.UseCaseRequest import UseCaseRequest


class UseCase(ABC):

    @abstractmethod
    def execute(self, uc_request: UseCaseRequest) -> None:
        pass
