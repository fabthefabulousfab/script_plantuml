global_packet=[]

class Global_packet(object):
	"""docstring for All_packet"""
	
	def __init__(self, prot,  fn, fd, src, dst):
		self._ip_src=src
		self._ip_dst=dst
		self._frame_number=fn
		self._frame_delta=fd
		self._prot=prot

	@property
	def ip_src(self):
	    return self._ip_src
	@ip_src.setter
	def ip_src(self, value):
	    self._ip_src = value

	@property
	def ip_dest(self):
	    return self._ip_dest
	@ip_dest.setter
	def ip_dest(self, value):
	    self._ip_dest = value
	
	@property
	def frame_number(self):
	    return self._frame_number
	@frame_number.setter
	def frame_number(self, value):
	    self._frame_number = value
	
	@property
	def frame_delta(self):
	    return self._frame_delta
	@frame_delta.setter
	def frame_delta(self, value):
	    self._frame_delta = value
	
	@property
	def prot(self):
	    return self._prot
	@prot.setter
	def prot(self, value):
	    self._prot = value
	
class Sip_packet(Global_packet):
	"""docstring for All_packet"""
	
	def __init__(self, prot, src, dst, fn, fd,md,rn):
		super(Sip_packet,self).__init__( prot, src, dst, fn, fd)
		self._method=md
		self._request_name=rn

	@property
	def method(self):
	    return self._method
	@method.setter
	def method(self, value):
	    self._method = value
	
	@property
	def request_name(self):
	    return self._request_name
	@request_name.setter
	def request_name(self, value):
	    self._request_name = value
	
	
	
	
				
