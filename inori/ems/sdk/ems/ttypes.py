#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class EMSErrorCode(object):
  """
  Exceptions
  """
  UNKNOWN_ERROR = 0
  DATABASE_ERROR = 1

  _VALUES_TO_NAMES = {
    0: "UNKNOWN_ERROR",
    1: "DATABASE_ERROR",
  }

  _NAMES_TO_VALUES = {
    "UNKNOWN_ERROR": 0,
    "DATABASE_ERROR": 1,
  }


class EMSUserException(TException):
  """
  Attributes:
   - error_code
   - error_name
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error_code', None, None, ), # 1
    (2, TType.STRING, 'error_name', None, None, ), # 2
    (3, TType.STRING, 'message', None, None, ), # 3
  )

  def __init__(self, error_code=None, error_name=None, message=None,):
    self.error_code = error_code
    self.error_name = error_name
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.error_name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EMSUserException')
    if self.error_code is not None:
      oprot.writeFieldBegin('error_code', TType.I32, 1)
      oprot.writeI32(self.error_code)
      oprot.writeFieldEnd()
    if self.error_name is not None:
      oprot.writeFieldBegin('error_name', TType.STRING, 2)
      oprot.writeString(self.error_name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 3)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error_code is None:
      raise TProtocol.TProtocolException(message='Required field error_code is unset!')
    if self.error_name is None:
      raise TProtocol.TProtocolException(message='Required field error_name is unset!')
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EMSSystemException(TException):
  """
  Attributes:
   - error_code
   - error_name
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error_code', None, None, ), # 1
    (2, TType.STRING, 'error_name', None, None, ), # 2
    (3, TType.STRING, 'message', None, None, ), # 3
  )

  def __init__(self, error_code=None, error_name=None, message=None,):
    self.error_code = error_code
    self.error_name = error_name
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.error_name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EMSSystemException')
    if self.error_code is not None:
      oprot.writeFieldBegin('error_code', TType.I32, 1)
      oprot.writeI32(self.error_code)
      oprot.writeFieldEnd()
    if self.error_name is not None:
      oprot.writeFieldBegin('error_name', TType.STRING, 2)
      oprot.writeString(self.error_name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 3)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error_code is None:
      raise TProtocol.TProtocolException(message='Required field error_code is unset!')
    if self.error_name is None:
      raise TProtocol.TProtocolException(message='Required field error_name is unset!')
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EMSUnknownException(TException):
  """
  Attributes:
   - error_code
   - error_name
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error_code', None, None, ), # 1
    (2, TType.STRING, 'error_name', None, None, ), # 2
    (3, TType.STRING, 'message', None, None, ), # 3
  )

  def __init__(self, error_code=None, error_name=None, message=None,):
    self.error_code = error_code
    self.error_name = error_name
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.error_name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EMSUnknownException')
    if self.error_code is not None:
      oprot.writeFieldBegin('error_code', TType.I32, 1)
      oprot.writeI32(self.error_code)
      oprot.writeFieldEnd()
    if self.error_name is not None:
      oprot.writeFieldBegin('error_name', TType.STRING, 2)
      oprot.writeString(self.error_name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 3)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error_code is None:
      raise TProtocol.TProtocolException(message='Required field error_code is unset!')
    if self.error_name is None:
      raise TProtocol.TProtocolException(message='Required field error_name is unset!')
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)