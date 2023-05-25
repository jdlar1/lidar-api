from enum import Enum


class Status(Enum, str):
    NOT_INITIALIZED = "not_initialized"
    ERROR = "error"
    OK = "ok"
