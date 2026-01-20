def enrol_module(modules, code):
  modules.add(code)
def is_enrolled(modules, code):
  if code in modules:
   return True
  else:
   return False
def drop_module(modules, code):
  modules.discard(code)
def count_modules(modules):
 return len(modules)