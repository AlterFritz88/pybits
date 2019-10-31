class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __init__(self, **kwargs):
        super(JsObject, self).__init__(**kwargs)
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __setattr__(self, key, value):
        self[key] = value
        self.__dict__[key] = value

    def update(self, __m, **kwargs) -> None:
        super(JsObject, self).update(__m, **kwargs)
        for k, v in __m.items():
            self.__dict__[k] = v


ob = JsObject(a=1, b=2, c=3)
print(ob['a'])
print(ob.b)
ob.d = 4
print(ob.d)
ob.update(dict(e=5))
print(ob.e)