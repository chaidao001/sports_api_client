from enum import Enum


class OrderProjection(Enum):
    ALL, EXECUTABLE, EXECUTION_COMPLETE = range(3)


class OrderBy(Enum):
    BY_MARKET, BY_MATCH_TIME, BY_PLACE_TIME, BY_SETTLED_TIME, BY_VOID_TIME = range(5)


class SortDir(Enum):
    EARLIEST_TO_LATEST, LATEST_TO_EARLIEST = range(2)


class OrderType(Enum):
    LIMIT, LIMIT_ON_CLOSE, MARKET_ON_CLOSE = range(3)


class Side(Enum):
    BACK, LAY = range(2)


class PersistenceType(Enum):
    LAPSE, PERSIST, MARKET_ON_CLOSE = range(3)


class ExecutionReportStatus(Enum):
    SUCCESS, FAILURE, PROCESSED_WITH_ERRORS, TIMEOUT = range(4)


class ExecutionReportErrorCode(Enum):
    ERROR_IN_MATCHER, PROCESSED_WITH_ERRORS, BET_ACTION_ERROR, INVALID_ACCOUNT_STATE, INVALID_WALLET_STATUS, \
    INSUFFICIENT_FUNDS, LOSS_LIMIT_EXCEEDED, MARKET_SUSPENDED, MARKET_NOT_OPEN_FOR_BETTING, DUPLICATE_TRANSACTION, \
    INVALID_ORDER, INVALID_MARKET_ID, PERMISSION_DENIED, DUPLICATE_BETIDS, NO_ACTION_REQUIRED, SERVICE_UNAVAILABLE, \
    REJECTED_BY_REGULATOR, NO_CHASING = range(18)


class InstructionReportStatus(Enum):
    SUCCESS, FAILURE, TIMEOUT = range(3)


class InstructionReportErrorCode(Enum):
    INVALID_BET_SIZE, INVALID_RUNNER, BET_TAKEN_OR_LAPSED, BET_IN_PROGRESS, RUNNER_REMOVED, \
    MARKET_NOT_OPEN_FOR_BETTING, LOSS_LIMIT_EXCEEDED, MARKET_NOT_OPEN_FOR_BSP_BETTING, INVALID_PRICE_EDIT, \
    INVALID_ODDS, INSUFFICIENT_FUNDS, INVALID_PERSISTENCE_TYPE, ERROR_IN_MATCHER, INVALID_BACK_LAY_COMBINATION, \
    ERROR_IN_ORDER, INVALID_BID_TYPE, INVALID_BET_ID, CANCELLED_NOT_PLACED, RELATED_ACTION_FAILED, \
    NO_ACTION_REQUIRED = range(20)
