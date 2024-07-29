class DefaultException:
    def __init__(self, *msg) -> None:
        if msg:
            self.message = msg[0]
        else:
            self.message = ""
    
    def __str__(self) -> str:
        return self.message
    

class PerformanceThresholdExceededException(DefaultException):
    """Performance Threshold Exceeded Exception"""
    pass


class ResourceExhaustionException(DefaultException):
    """Resource Exhaustion Exception"""
    pass


class HighLatencyException(DefaultException):
    """High Latency Exception"""
    pass


class LowThroughputException(DefaultException):
    """Low Throughput Exception"""
    pass


class MemoryUsageExceededException(DefaultException):
    """Memory Usage Exceeded Exception"""
    pass


class CPUUsageExceededException(DefaultException):
    """CPU Usage Exceeded Exception"""
    pass


class DiskIOException(DefaultException):
    """Disk IO Exception"""
    pass


class NetworkBandwidthExceededException(DefaultException):
    """Network Bandwidth Exceeded Exception"""
    pass


class CacheMissException(DefaultException):
    """Cache Miss Exception"""
    pass


class OptimizationException(DefaultException):
    """Optimization Exception"""
    pass
