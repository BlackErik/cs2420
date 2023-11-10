
class Student:
    def __init__( self, last, first, ssn, email, age ):
        self.mLast = last
        self.mFirst = first
        self.mSsn = ssn
        self.mEmail = email
        self.mAge = age

    def __eq__( self, rhs ):
        return self.mSsn == rhs.mSsn
    def __lt__( self ,rhs):
        return self.mSsn < rhs.mSsn

    def __le__( self, rhs ):
        return self.mSsn <= rhs.mSsn 
    def __gt__( self, rhs ):
        return self.mSsn > rhs.mSsn

    def __ge__( self, rhs ):
        return self.mSsn >= rhs.mSsn

    def __nq__( self, rhs ):
        return self.mSsn != rhs.mSsn