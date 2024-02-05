metamaker = (lambda meta, cls: ( lambda: [ (dict_.pop(es, None) for es in dict_.get("__slots__", tuple())) if [None for [globals()["dict_"]] in [[dict(cls.__dict__)]]][0] is None else None, [None for [globals()["dict_"]["__metaclass"]] in [[meta]]], [None for [globals()["dict_"]["__wrapped__"]] in [[cls]]], meta(str(cls.__name__), tuple(cls.__bases__), dict_), ][-1]))
printf = lambda format_string, *args: print(format_string,end="") if not args else print(format_string % args,end="")
main = metamaker(type("b", (type,), {"__call__": lambda self, _: {None}}), type("", (object,), {}))()
int = metamaker(type("a", (type,), {"__sub__": lambda self2, _: {None} if isinstance(_, set) else [None for [globals()[_.split("=")[0]]] in [[__import__('builtins').int(_.split("=")[1])]]][0]}), type("a", (object,), {}))()
void = None
return_0 = None




int-main(void)-{
  printf("Hello, World!\n"),

  int-"num1=2",
  int-"num2=3",

  printf("%d + %d = %d\n", num1, num2, num1+num2),
  return_0
}