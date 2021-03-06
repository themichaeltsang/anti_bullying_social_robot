"""autogenerated by genpy from clm_bridge/ClmHeadPose.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ClmHeadPose(genpy.Message):
  _md5sum = "359ad24d008c072a21ffe199b86dc8c4"
  _type = "clm_bridge/ClmHeadPose"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 pitch
float32 yaw
float32 roll
float32 x
float32 y
float32 z
"""
  __slots__ = ['pitch','yaw','roll','x','y','z']
  _slot_types = ['float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pitch,yaw,roll,x,y,z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ClmHeadPose, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pitch is None:
        self.pitch = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.roll is None:
        self.roll = 0.
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.z is None:
        self.z = 0.
    else:
      self.pitch = 0.
      self.yaw = 0.
      self.roll = 0.
      self.x = 0.
      self.y = 0.
      self.z = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.pitch, _x.yaw, _x.roll, _x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.pitch, _x.yaw, _x.roll, _x.x, _x.y, _x.z,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6f.pack(_x.pitch, _x.yaw, _x.roll, _x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.pitch, _x.yaw, _x.roll, _x.x, _x.y, _x.z,) = _struct_6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6f = struct.Struct("<6f")
