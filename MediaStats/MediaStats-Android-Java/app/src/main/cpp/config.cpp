//
// Created by Wenchao Ding on 2020-09-03.
//

#include <jni.h>
#include <string>

extern "C"
JNIEXPORT jstring
JNICALL
Java_com_netease_mediastats_NativeConfig_getAppKey__(JNIEnv *env, jclass) {
    std::string appKey = "your APP ley";
    return env->NewStringUTF(appKey.c_str());
}