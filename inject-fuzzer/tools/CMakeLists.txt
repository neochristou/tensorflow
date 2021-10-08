# THE LIST OF TOOLS AND THE CORRESPONDING SOURCE FILES
# ====================================================
set(INJECT_FUZZER_TOOLS
    inject-fuzzer
)


set(inject-fuzzer_SOURCES
    InjectFuzzerMain.cpp
  ../lib/InjectFuzzer.cpp
)

# CONFIGURE THE TOOLS
# ===================
foreach( tool ${INJECT_FUZZER_TOOLS} )
    # Create a library corresponding to 'plugin'
    add_executable(
      ${tool}
      ${${tool}_SOURCES}
      )

    # Link with libclangTooling
    target_link_libraries(
      ${tool}
      clangTooling
    )

    # Configure include directories for 'tool'
    target_include_directories(
      ${tool}
      PRIVATE
      "${CMAKE_CURRENT_SOURCE_DIR}/../include"
    )
endforeach()
