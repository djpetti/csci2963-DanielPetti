#CMake Tutorial

##Step 1

###tutorial.cxx

```
// A simple program that computes the square root of a number
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    fprintf(stdout,"Usage: %s number\n",argv[0]);
    return 1;
    }
  double inputValue = atof(argv[1]);
  double outputValue = sqrt(inputValue);
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}
```

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
add_executable(Tutorial tutorial.cxx)
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- The C compiler identification is GNU 4.9.3
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
Scanning dependencies of target Tutorial
[ 50%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile  Tutorial
```

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the executable
add_executable(Tutorial tutorial.cxx)
```

###TutorialConfig.h.in

```
// the configured options and settings for Tutorial
#define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
#define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
```

###tutorial.cxx

```
// A simple program that computes the square root of a number
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "TutorialConfig.h"

int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    fprintf(stdout,"%s Version %d.%d\n",
            argv[0],
            Tutorial_VERSION_MAJOR,
            Tutorial_VERSION_MINOR);
    fprintf(stdout,"Usage: %s number\n",argv[0]);
    return 1;
    }
  double inputValue = atof(argv[1]);
  double outputValue = sqrt(inputValue);
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
Scanning dependencies of target Tutorial
[ 50%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial
./Tutorial Version 1.0
Usage: ./Tutorial number
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial 10
The square root of 10 is 3.16228
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```

##Step 2

###MathFunctions/CMakeLists.txt

```
add_library(MathFunctions mysqrt.cxx)
```

###MathFunctions/mysqrt.cxx

```
#include "MathFunctions.h"
#include <stdio.h>

// a hack square root calculation using simple operations
double mysqrt(double x)
{
  if (x <= 0) {
    return 0;
  }

  double result;
  double delta;
  result = x;

  // do ten iterations
  int i;
  for (i = 0; i < 10; ++i) {
    if (result <= 0) {
      result = 0.1;
    }
    delta = x - (result * result);
    result = result + 0.5 * delta / result;
    fprintf(stdout, "Computing sqrt of %g to be %g\n", x, result);
  }
  return result;
}
```

###MathFunctions/MathFunctions.h

```
double mysqrt(double x);
```

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
add_subdirectory (MathFunctions)

# add the executable
add_executable(Tutorial tutorial.cxx)
target_link_libraries (Tutorial MathFunctions)
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial
./Tutorial Version 1.0
Usage: ./Tutorial number
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial 42
The square root of 42 is 6.48074
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```

Making the MathFunctions library optional:

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# should we use our own math functions?
option (USE_MYMATH
        "Use tutorial provided math implementation" ON)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# add the executable
add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})
```

###tutorial.cxx

```
// A simple program that computes the square root of a number
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "TutorialConfig.h"
#ifdef USE_MYMATH
#include "MathFunctions.h"
#endif

int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    fprintf(stdout,"%s Version %d.%d\n", argv[0],
            Tutorial_VERSION_MAJOR,
            Tutorial_VERSION_MINOR);
    fprintf(stdout,"Usage: %s number\n",argv[0]);
    return 1;
    }

  double inputValue = atof(argv[1]);

#ifdef USE_MYMATH
  double outputValue = mysqrt(inputValue);
#else
  double outputValue = sqrt(inputValue);
#endif

  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial 24
The square root of 24 is 4.89898
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```

##Step 3

###MathFunctions/CMakeLists.txt

```
add_library(MathFunctions mysqrt.cxx)

install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)
```

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# should we use our own math functions?
option (USE_MYMATH
        "Use tutorial provided math implementation" ON)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# add the executable
add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

# add the install targets
install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
         DESTINATION include)
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ sudo make install
[sudo] password for daniel:
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
Install the project...
-- Install configuration: ""
-- Installing: /usr/local/bin/Tutorial
-- Installing: /usr/local/include/TutorialConfig.h
-- Installing: /usr/local/bin/libMathFunctions.a
-- Installing: /usr/local/include/MathFunctions.h
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ Tutorial
Tutorial Version 1.0
Usage: Tutorial number
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ Tutorial 1
The square root of 1 is 1
```

Adding tests to the project:

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# should we use our own math functions?
option (USE_MYMATH
        "Use tutorial provided math implementation" ON)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# add the executable
add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

# add the install targets
install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
         DESTINATION include)

include(CTest)

# does the application run
add_test (TutorialRuns Tutorial 25)

# does it sqrt of 25
add_test (TutorialComp25 Tutorial 25)
set_tests_properties (TutorialComp25 PROPERTIES PASS_REGULAR_EXPRESSION "25 is 5")

# does it handle negative numbers
add_test (TutorialNegative Tutorial -25)
set_tests_properties (TutorialNegative PROPERTIES PASS_REGULAR_EXPRESSION "-25 is 0")

# does it handle small numbers
add_test (TutorialSmall Tutorial 0.0001)
set_tests_properties (TutorialSmall PROPERTIES PASS_REGULAR_EXPRESSION "0.0001 is 0.01")

# does the usage message work?
add_test (TutorialUsage Tutorial)
set_tests_properties (TutorialUsage PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number")
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ctest
Test project /home/daniel/git/open_source/csci2963-DanielPetti/code/build
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialComp25
2/5 Test #2: TutorialComp25 ...................   Passed    0.00 sec
    Start 3: TutorialNegative
3/5 Test #3: TutorialNegative .................***Failed  Required regular expression not found.Regex=[-25 is 0
]  0.00 sec
    Start 4: TutorialSmall
4/5 Test #4: TutorialSmall ....................   Passed    0.00 sec
    Start 5: TutorialUsage
5/5 Test #5: TutorialUsage ....................   Passed    0.00 sec

80% tests passed, 1 tests failed out of 5

Total Test time (real) =   0.01 sec

The following tests FAILED:
	  3 - TutorialNegative (Failed)
Errors while running CTest
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```

##Step 4

###CMakeLists.txt

```
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# should we use our own math functions?
option (USE_MYMATH
        "Use tutorial provided math implementation" ON)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# add the executable
add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

# add the install targets
install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
         DESTINATION include)

# does this system provide the log and exp functions?
include (CheckFunctionExists)
check_function_exists (log HAVE_LOG)
check_function_exists (exp HAVE_EXP)

include(CTest)

# does the application run
add_test (TutorialRuns Tutorial 25)

# does it sqrt of 25
add_test (TutorialComp25 Tutorial 25)
set_tests_properties (TutorialComp25 PROPERTIES PASS_REGULAR_EXPRESSION "25 is 5")

# does it handle negative numbers
add_test (TutorialNegative Tutorial -25)
set_tests_properties (TutorialNegative PROPERTIES PASS_REGULAR_EXPRESSION "-25 is 0")

# does it handle small numbers
add_test (TutorialSmall Tutorial 0.0001)
set_tests_properties (TutorialSmall PROPERTIES PASS_REGULAR_EXPRESSION "0.0001 is 0.01")

# does the usage message work?
add_test (TutorialUsage Tutorial)
set_tests_properties (TutorialUsage PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number")
```

###TutorialConfig.h.in

```
// the configured options and settings for Tutorial
#define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
#define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@

// does the platform provide exp and log functions?
#cmakedefine HAVE_LOG
#cmakedefine HAVE_EXP
```

###MathFunctions/mysqrt.h

```
#include "MathFunctions.h"
#include <stdio.h>

// a hack square root calculation using simple operations
double mysqrt(double x)
{
  if (x <= 0) {
    return 0;
  }

  double result;
  double delta;
  result = x;

	// if we have both log and exp then use them
	#if defined (HAVE_LOG) && defined (HAVE_EXP)
		result = exp(log(x)*0.5);
	#else // otherwise use an iterative approach

  // do ten iterations
  int i;
  for (i = 0; i < 10; ++i) {
    if (result <= 0) {
      result = 0.1;
    }
    delta = x - (result * result);
    result = result + 0.5 * delta / result;
    fprintf(stdout, "Computing sqrt of %g to be %g\n", x, result);
  }

	#endif

  return result;
}
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ ./Tutorial 25
The square root of 25 is 5
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```

##Step 5

###MakeTable.cxx

```
// A simple program that builds a sqrt table
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
  int i;
  double result;

  // make sure we have enough arguments
  if (argc < 2)
    {
    return 1;
    }

  // open the output file
  FILE *fout = fopen(argv[1],"w");
  if (!fout)
    {
    return 1;
    }

  // create a source file with a table of square roots
  fprintf(fout,"double sqrtTable[] = {\n");
  for (i = 0; i < 10; ++i)
    {
    result = sqrt(static_cast<double>(i));
    fprintf(fout,"%g,\n",result);
    }

  // close the table with a zero
  fprintf(fout,"0};\n");
  fclose(fout);
  return 0;
}
```

###MathFunctions/CMakeLists.txt

```
# first we add the executable that generates the table
add_executable(MakeTable MakeTable.cxx)

# add the command to generate the source code
add_custom_command (
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  DEPENDS MakeTable
  )

# add the binary tree directory to the search path for
# include files
include_directories( ${CMAKE_CURRENT_BINARY_DIR} )

# add the main library
add_library(MathFunctions mysqrt.cxx ${CMAKE_CURRENT_BINARY_DIR}/Table.h  )

install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)
```

###Output

```
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/daniel/git/open_source/csci2963-DanielPetti/code/build
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$ make -j8
Scanning dependencies of target MakeTable
[ 14%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
[ 28%] Linking CXX executable MakeTable
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 57%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 71%] Linking CXX static library libMathFunctions.a
[ 71%] Built target MathFunctions
[ 85%] Linking CXX executable Tutorial
[100%] Built target Tutorial
daniel@RainbowDash:~/git/open_source/csci2963-DanielPetti/code/build$
```
