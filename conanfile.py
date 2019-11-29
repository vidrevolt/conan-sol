from conans import ConanFile, CMake, tools
import os


class LibLoConan(ConanFile):
    name = "sol"
    description = "A C++ <-> Lua API wrapper with advanced features and top notch performance"
    topics = ("conan", "sol", "sol2", "sol3", "lua")
    url = "https://github.com/vidrevolt/conan-sol"
    homepage = "https://github.com/ThePhD/sol2"
    no_copy_source = True

    _source_subfolder = "sol"

    def system_requirements(self):
        installer = tools.SystemPackageTool()
        if tools.os_info.is_linux and tools.os_info.with_apt:
            installer.install("lua5.3")
            installer.install("liblua5.3-dev")
        elif tools.os_info.with_pacman:
            installer.install("lua")
        elif tools.os_info.with_brew:
            installer.install("lua")


    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "2-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "single/include/")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
