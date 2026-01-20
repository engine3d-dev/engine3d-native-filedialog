import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy

class NativeFileDialog(ConanFile):
    name = "nfd"
    version = "3.0"
    package_type = "library"
    license = "Appache-2.0"
    homepage = "https://github.com/engine3d-dev/nfd"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "CMakeLists.txt", "nfd/*", "src/*"

    # Putting all of your build-related dependencies here
    # def build_requirements(self):
    #     self.tool_requires("ninja/1.13.1")
    #     self.tool_requires("cmake/4.1.2")
    #     self.tool_requires("engine3d-cmake-utils/4.0")
    def build_requirements(self):
        # self.tool_requires("make/4.4.1")
        # self.tool_requires("cmake/4.1.1")
        # self.tool_requires("engine3d-cmake-utils/4.0")
        self.tool_requires("cmake/4.1.2")
        self.tool_requires("ninja/1.13.1")
        self.tool_requires("engine3d-cmake-utils/4.0")
        self.tool_requires("cmake-modules-toolchain/1.0.3")
    
    # This is how exporting the sources work
    # def export_sources(self):
    #     copy(self,"CMakeLists.txt", self.recipe_folder, self.export_sources_folder)
    #     copy(self,"*h", self.recipe_folder, self.export_sources_folder)
    #     copy(self,"*.cpp", self.recipe_folder, self.export_sources_folder)

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
    
    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        # If you use "MinGW Makefiles" on windows, by default looks for mingw32-make.exe instead.
        # Needed to find make.exe installed by choco
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, pattern="*.h", src=os.path.join(self.source_folder, "nfd"), dst=os.path.join(self.package_folder, "nfd"))
        copy(self, pattern="*.a", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.so", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.lib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.dll", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"), keep_path=False)
        copy(self, pattern="*.dylib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        cmake = CMake(self)
        cmake.install()
    
    def package_info(self):
        self.cpp_info.set_property("cmake_target_name", "nfd::nfd")
        self.cpp_info.libs = ["nfd"]
        self.cpp_info.includedirs = ['./', './nfd']
