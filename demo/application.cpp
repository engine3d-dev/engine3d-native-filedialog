#include <iostream>
#include <engine3d-nfd/nfd.h>
#include <print>
using namespace std;

static std::string LoadFile(const char* p_Filter){
    char* output_path = nullptr;
    std::string filter = "obj";

    auto result = NFD_OpenDialog(filter.c_str(), nullptr, &output_path);

    // if(result == NFD_OKAY){
    //     printf("Okay!\n");
    //     // printf("%s")
    //     std::print("Output Path = {}\n", output_path);
    //     std::print("Filter = {}", filter);
    // }

    if(result == NFD_OKAY){
        std::print("Error Loading File!\n");
        return std::string(output_path);
    }

    // 
    return "";
}

int main(){
    std::string file = LoadFile("obj;gltf;fbx");
    std::print("Loaded File = {}", file);
    return 0;
}