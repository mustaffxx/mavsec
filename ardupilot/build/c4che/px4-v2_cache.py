AP_LIBRARIES = ['AP_UAVCAN', 'modules/uavcan/libuavcan/src/**/*.cpp', 'AP_HAL_PX4']
AP_LIBRARIES_OBJECTS_KW = {'features': ['px4_ap_library']}
AP_PROGRAM_AS_STLIB = True
AP_PROGRAM_FEATURES = ['px4_ap_program']
AR = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'px4-v2'
BOOTLOADER = False
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '9', '3')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-MMD']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CMAKE = ['/usr/bin/cmake']
CMAKE_GENERATOR_OPTION = '-GUnix Makefiles'
CMAKE_MIN_VERSION = '3.2'
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=format-security', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=switch', '-Werror=sign-compare', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=unused-but-set-variable', '-Wno-error=cast-align', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-MMD']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/azzathesis/ardupilot"', 'CONFIG_HAL_BOARD=HAL_BOARD_PX4', 'HAVE_OCLOEXEC=0', 'HAVE_STD_NULLPTR_T=0', 'UAVCAN_CPP_VERSION=UAVCAN_CPP03', 'UAVCAN_NO_ASSERTIONS=1', 'UAVCAN_NULLPTR=nullptr']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_CMATH_ISINF': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'WAF_BUILD': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', '__STDC_FORMAT_MACROS': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'PYTHONDIR': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISNAN': '', '_GNU_SOURCE': '', 'PYTHONARCHDIR': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
DSDL_COMPILER = '/home/azzathesis/ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/azzathesis/ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['PX4Firmware', 'PX4NuttX', 'uavcan', 'mavlink']
HAS_GTEST = False
INCLUDES = ['/home/azzathesis/ardupilot/libraries/', '/home/azzathesis/ardupilot/libraries/AP_Common/missing', '/home/azzathesis/ardupilot/modules/uavcan/libuavcan/include']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-Wl,--gc-sections']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-gcc']
LINK_CXX = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-g++']
MAKE = ['/usr/bin/make']
MAVGEN = '/home/azzathesis/ardupilot/modules/mavlink/pymavlink/tools/mavgen.py'
MAVLINK_DIR = '/home/azzathesis/ardupilot/modules/mavlink'
PREFIX = '/usr'
PX4IO_ELF_DEST = 'px4-extra-files/px4io'
PX4_ADD_GIT_HASHES = '/home/azzathesis/ardupilot/Tools/scripts/add_git_hashes.py'
PX4_APM_ROOT = '/home/azzathesis/ardupilot'
PX4_BOARD_NAME = 'px4fmu-v2'
PX4_BOARD_RC = False
PX4_BOOTLOADER = '/../../../Tools/bootloaders/px4fmuv2_bl.bin'
PX4_BOOTLOADER_NAME = 'px4fmuv2_bl.bin'
PX4_CMAKE_VARS = {'PX4_NUTTX_ROMFS': '/home/azzathesis/ardupilot/build/px4-v2/px4-extra-files/ROMFS', 'EXTRA_CXX_FLAGS': '-Wno-error=double-promotion -Wno-error=reorder -DCMAKE_BUILD -DARDUPILOT_BUILD -I/home/azzathesis/ardupilot/build/px4-v2/libraries/GCS_MAVLink -I/home/azzathesis/ardupilot/build/px4-v2/libraries/GCS_MAVLink/include/mavlink -Wl,--gc-sections', 'CONFIG': 'nuttx_px4fmu-v2_apm', 'CMAKE_MODULE_PATH': '/home/azzathesis/ardupilot/Tools/ardupilotwaf/px4/cmake', 'EXTRA_C_FLAGS': '-DCMAKE_BUILD', 'NUTTX_SRC': '/home/azzathesis/ardupilot/modules/PX4NuttX', 'ARDUPILOT_BUILD': 'YES'}
PX4_NUTTX_ROOT = '/home/azzathesis/ardupilot/modules/PX4NuttX'
PX4_PARAM_DEFAULTS = None
PX4_PX4IO_NAME = 'px4io-v2'
PX4_RC_S_SCRIPT = 'init.d/rcS'
PX4_ROMFS_BLD = 'px4-extra-files/ROMFS'
PX4_ROMFS_SRC = 'mk/PX4/ROMFS'
PX4_ROOT = '/home/azzathesis/ardupilot/modules/PX4Firmware'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/lib/python2.7/dist-packages'
PYTHONDIR = '/usr/lib/python2.7/dist-packages'
PYTHON_VERSION = '2.7'
ROMFS_EXCLUDE = ['oreoled.bin']
ROMFS_FILES = []
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-size']
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'arm-none-eabi'
cfg_files = ['/home/azzathesis/ardupilot/build/px4-v2/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
