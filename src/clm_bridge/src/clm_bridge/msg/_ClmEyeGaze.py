"""autogenerated by genpy from clm_bridge/ClmEyeGaze.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ClmEyeGaze(genpy.Message):
  _md5sum = "b0f4e23f8acc1cfa57687d7b0276b35e"
  _type = "clm_bridge/ClmEyeGaze"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 RIGHT_EYE = 0
uint8 LEFT_EYE = 1

uint8 eye_id

float32 gaze_direction_cameraref_x
float32 gaze_direction_cameraref_y
float32 gaze_direction_cameraref_z

float32 gaze_direction_headref_x
float32 gaze_direction_headref_y
float32 gaze_direction_headref_z
"""
  # Pseudo-constants
  RIGHT_EYE = 0
  LEFT_EYE = 1

  __slots__ = ['eye_id','gaze_direction_cameraref_x','gaze_direction_cameraref_y','gaze_direction_cameraref_z','gaze_direction_headref_x','gaze_direction_headref_y','gaze_direction_headref_z']
  _slot_types = ['uint8','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       eye_id,gaze_direction_cameraref_x,gaze_direction_cameraref_y,gaze_direction_cameraref_z,gaze_direction_headref_x,gaze_direction_headref_y,gaze_direction_headref_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ClmEyeGaze, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.eye_id is None:
        self.eye_id = 0
      if self.gaze_direction_cameraref_x is None:
        self.gaze_direction_cameraref_x = 0.
      if self.gaze_direction_cameraref_y is None:
        self.gaze_direction_cameraref_y = 0.
      if self.gaze_direction_cameraref_z is None:
        self.gaze_direction_cameraref_z = 0.
      if self.gaze_direction_headref_x is None:
        self.gaze_direction_headref_x = 0.
      if self.gaze_direction_headref_y is None:
        self.gaze_direction_headref_y = 0.
      if self.gaze_direction_headref_z is None:
        self.gaze_direction_headref_z = 0.
    else:
      self.eye_id = 0
      self.gaze_direction_cameraref_x = 0.
      self.gaze_direction_cameraref_y = 0.
      self.gaze_direction_cameraref_z = 0.
      self.gaze_direction_headref_x = 0.
      self.gaze_direction_headref_y = 0.
      self.gaze_direction_headref_z = 0.

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
      buff.write(_struct_B6f.pack(_x.eye_id, _x.gaze_direction_cameraref_x, _x.gaze_direction_cameraref_y, _x.gaze_direction_cameraref_z, _x.gaze_direction_headref_x, _x.gaze_direction_headref_y, _x.gaze_direction_headref_z))
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
      end += 25
      (_x.eye_id, _x.gaze_direction_cameraref_x, _x.gaze_direction_cameraref_y, _x.gaze_direction_cameraref_z, _x.gaze_direction_headref_x, _x.gaze_direction_headref_y, _x.gaze_direction_headref_z,) = _struct_B6f.unpack(str[start:end])
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
      buff.write(_struct_B6f.pack(_x.eye_id, _x.gaze_direction_cameraref_x, _x.gaze_direction_cameraref_y, _x.gaze_direction_cameraref_z, _x.gaze_direction_headref_x, _x.gaze_direction_headref_y, _x.gaze_direction_headref_z))
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
      end += 25
      (_x.eye_id, _x.gaze_direction_cameraref_x, _x.gaze_direction_cameraref_y, _x.gaze_direction_cameraref_z, _x.gaze_direction_headref_x, _x.gaze_direction_headref_y, _x.gaze_direction_headref_z,) = _struct_B6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B6f = struct.Struct("<B6f")
