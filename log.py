import logging


def configure_logger(lg, level, log_format=None, propagate=False):
    if not log_format:
        log_format = '%(name)s\t%(levelname)s\t%(asctime)s\t[%(funcName)s] %(message)s'
    lg.setLevel(level)
    hdr = logging.StreamHandler()
    hdr.setFormatter(logging.Formatter(log_format, '%Y-%m-%dT%H:%M:%S'))
    lg.addHandler(hdr)
    lg.propagate = propagate


def set_logger(
    name,
    level='INFO',
    fmt='%(asctime)s [%(levelname)-5s] %(name)s: %(message)s',
    datefmt=None,
    propagate=True,
    remove_handlers=False):
    """
    This function will clear the previous handlers and set only one handler,
    which will only be StreamHandler for the logger.

    This function is designed to be able to called multiple times in a context.

    Note that if a logger has no handlers, it will be added a handler automatically when it is used.
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))
    logger.propagate = propagate

    if remove_handlers:
        logger.handlers = []
        return

    handler = None
    for h in logger.handlers:
        if isinstance(h, logging.StreamHandler):
            # use existing instead of clean and create
            handler = h
            break
    if not handler:
        handler = logging.StreamHandler()
        logger.addHandler(handler)

    formatter_kwgs = {}
    if fmt is not None:
        formatter_kwgs['fmt'] = fmt
    if datefmt is not None:
        formatter_kwgs['datefmt'] = datefmt
    handler.setFormatter(logging.Formatter(**formatter_kwgs))
