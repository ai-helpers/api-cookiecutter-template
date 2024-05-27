from typing import Optional


class OperationResult:
    def __init__(self, successful: Optional[bool] = None,
                 message: Optional[str] = None):
        self._successful = successful
        self._message = message

    def __add__(self, other):
        successfulness = [s._successful
                          for s in [self, other]
                          if s._successful is not None]
        successful = all(successfulness) if len(successfulness) > 0 else None
        message = " ".join([s._message
                            for s in [self, other]
                            if s._message is not None])
        return OperationResult(successful=successful, message=message)

    def __bool__(self) -> bool:
        return self._successful

    def __str__(self) -> str:
        return self._message

    def was_successful(self) -> bool:
        return bool(self)