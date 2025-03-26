#ifndef GO
#error Nope
#endif

#include "config-host.h"

GO("libEGL.so.1", libegl)
#ifndef CONFIG_LOONGARCH_NEW_WORLD
GO("libdl.so.2", libdl)
#endif
//GO("libgtk-3.so", gtk3)
//GO("libgio-2.0.so", gio2)
GO("libc.so.6", libc)
GO("libGL.so.1", libgl)
GO("libX11.so.6", libx11)
GO("libGLU.so.1", libglu)
GO("libGLX.so.0", libglx)
GO("libXxf86vm.so.1", libxxf86vm)
GO("libXext.so.6", libxext)
GO("libXau.so.6", libxau)
GO("libXi.so.6", libxi)
GO("libXdmcp.so.6", libxdmcp)
GO("libxshmfence.so.1", xshmfence)
GO("libXfixes.so.3", libxfixes)
GO("libXcursor.so.1", libxcursor)
GO("libXinerama.so.1", xinerama)
GO("libXrandr.so.2", libxrandr)
GO("libXss.so.1", libxss)
GO("libXft.so.2", libxft)
GO("libXtst.so.6", libxtst)
GO("libXt.so.6", libxt)
GO("libXrender.so.1", libxrender)
GO("libXpm.so.4", libxpm)
GO("libXdamage.so.1", libxdamage)
GO("libXmu.so.6", libxmu)
GO("libXcomposite.so.1", libxcomposite)
GO("libva-x11.so.2", libvax11)
GO("libva-drm.so.2", libvadrm)
GO("libva.so.2", libva)
GO("libxcb.so.1", libxcb)
GO("libxcb-xkb.so.1", libxcbxkb)
//GO("libxkbcommon-x11.so.0", xkbcommonx11)
//GO("libxkbcommon.so.0", xkbcommon)
GO("libX11-xcb.so.1", libx11xcb)
GO("libxcb-randr.so.0", libxcbrandr)
GO("libxcb-shm.so.0", libxcbshm)
GO("libxcb-xfixes.so.0", libxcbxfixes)
GO("libxcb-shape.so.0", libxcbshape)
GO("libxcb-image.so.0", libxcbimage)
GO("libxcb-keysyms.so.1", libxcbkeysyms)
GO("libxcb-xtest.so.0", libxcbxtest)
GO("libxcb-glx.so.0", libxcbglx)
GO("libxcb-dri2.so.0", libxcbdri2)
GO("libxcb-dri3.so.0", libxcbdri3)
GO("libvulkan.so.1", vulkan)
GO("libxcb-cursor.so.0", libxcbcursor)
GO("libxcb-icccm.so.4", libxcbicccm)
GO("libxcb-util.so.1", libxcbutil)
GO("libxcb-render-util.so.0", libxcbrenderutil)
GO("libxcb-render.so.0", libxcbrender)
GO("libxcb-sync.so.1", libxcbsync)
GO("libxcb-xinerama.so.0", libxcbxinerama)
GO("libxcb-xinput.so.0", libxcbxinput)
GO("libxcb-present.so.0", libxcbpresent)


GOALIAS("libxcb-cursor.so", libxcbcursor)
GOALIAS("libxcb-icccm.so", libxcbicccm)
GOALIAS("libxcb-util.so", libxcbutil)
GOALIAS("libxcb-render-util.so", libxcbrenderutil)
GOALIAS("libxcb-render.so", libxcbrender)
GOALIAS("libxcb-sync.so", libxcbsync)
GOALIAS("libxcb-xinerama.so", libxcbxinerama)
GOALIAS("libxcb-xinput.so", libxcbxinput)
GOALIAS("libxcb-present.so", libxcbpresent)
GOALIAS("libvulkan.so", vulkan)
GOALIAS("libEGL.so", libegl)
#ifndef CONFIG_LOONGARCH_NEW_WORLD
GOALIAS("libdl.so", libdl)
#endif
//GOALIAS("libgtk-3.so", gtk3)
//GOALIAS("libgio-2.0.so", gio2)
GOALIAS("libc.so", libc)
GOALIAS("libGL.so", libgl)
GOALIAS("libX11.so", libx11)
GOALIAS("libGLU.so", libglu)
GOALIAS("libGLX.so", libglx)
GOALIAS("libXxf86vm.so", libxxf86vm)
GOALIAS("libXext.so", libxext)
GOALIAS("libXau.so", libxau)
GOALIAS("libXi.so", libxi)
GOALIAS("libXdmcp.so", libxdmcp)
GOALIAS("libxshmfence.so", xshmfence)
GOALIAS("libXfixes.so", libxfixes)
GOALIAS("libXcursor.so", libxcursor)
GOALIAS("libXinerama.so", xinerama)
GOALIAS("libXrandr.so", libxrandr)
GOALIAS("libXss.so", libxss)
GOALIAS("libXft.so", libxft)
GOALIAS("libXtst.so", libxtst)
GOALIAS("libXt.so", libxt)
GOALIAS("libXrender.so", libxrender)
GOALIAS("libXpm.so", libxpm)
GOALIAS("libXdamage.so", libxdamage)
GOALIAS("libXmu.so", libxmu)
GOALIAS("libXcomposite.so", libxcomposite)
GOALIAS("libva-x11.so", libvax11)
GOALIAS("libva-drm.so", libvadrm)
GOALIAS("libva.so", libva)
GOALIAS("libxcb.so", libxcb)
GOALIAS("libxcb-xkb.so", libxcbxkb)
//GOALIAS("libxkbcommon-x11.so", xkbcommonx11)
//GOALIAS("libxkbcommon.so", xkbcommon)
GOALIAS("libX11-xcb.so", libx11xcb)
GOALIAS("libxcb-randr.so", libxcbrandr)
GOALIAS("libxcb-shm.so", libxcbshm)
GOALIAS("libxcb-xfixes.so", libxcbxfixes)
GOALIAS("libxcb-shape.so", libxcbshape)
GOALIAS("libxcb-image.so", libxcbimage)
GOALIAS("libxcb-keysyms.so", libxcbkeysyms)
GOALIAS("libxcb-xtest.so", libxcbxtest)
GOALIAS("libxcb-glx.so", libxcbglx)
GOALIAS("libxcb-dri2.so", libxcbdri2)
GOALIAS("libxcb-dri3.so", libxcbdri3)
