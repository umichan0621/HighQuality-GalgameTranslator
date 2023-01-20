#include <gal_translator.h>
#include <glog/logging.h>

int main(int argc, char* argv[]) {
    // Initialize Google’s logging library.
    google::InitGoogleLogging(argv[0]);
    FLAGS_log_dir = "./logs/";
    FLAGS_stderrthreshold = 1;
    FLAGS_colorlogtostderr = true;
    google::SetLogDestination(google::INFO, "./logs/info_");
    google::SetLogDestination(google::WARNING, "./logs/warn_");
    google::SetLogDestination(google::ERROR, "./logs/error_");
    google::SetLogDestination(google::FATAL, "./logs/fatal_");
    google::SetLogFilenameExtension(".log");

    gal::GalTranslator gal_translator;

    LOG(WARNING) << "Hello,GLOG!";
    LOG(INFO) << "Hello,GLOG!";
    LOG(ERROR) << "Hello,GLOG!";
    google::ShutdownGoogleLogging();
}
