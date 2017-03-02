class Feed(object):
    _uid = None
    _ltp = None

    def set_uid(self, uid):
        if type(uid) == str:
            self._uid = uid
        else:
            raise IOError("Only strings allowed for uid, %s found" % (type(uid), ))

    def get_uid(self):
        return self._uid

    def set_ltp(self, ltp):
        if type(price) == float:
            self._ltp = ltp
        elif type(price) == int:
            self._ltp = float(ltp)
        else:
            raise IOError("Only floats allowed for ltp, %s found" % (type(ltp), ))

    def get_ltp(self):
        return self._ltp
