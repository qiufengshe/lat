#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>

#include "wrappedlibs.h"

#include "wrapper.h"
#include "bridge.h"
#include "library_private.h"

const char* libxauName = "libXau.so.6";
#define LIBNAME libxau


#include "wrappedlib_init.h"

