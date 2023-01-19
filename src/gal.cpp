#include <gal_translator.h>

int main() {
    gal::GalTranslator gal_translator;
    gal_translator.LoadConfig("/home/autowise/HighQuality-GalgameTranslator/config/");
    gal_translator.SetFile("/home/autowise/HighQuality-GalgameTranslator/q.txt");
    gal_translator.Translate();
}
