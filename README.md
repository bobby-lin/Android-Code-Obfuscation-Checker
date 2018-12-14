# Android-Code-Obfuscation-Checker
Automate the code obfuscation testing process using written rule packs

Code Obfuscation is one of the methods to defend against Reverse Engineering of Android APK.  Currently many decompilers are available for free. However, developers and security testers often have to manually verify the decompiled APK in order to see if code obfuscation is turned on correctly. The Android Code Obfuscation Checker is able to automate the process (from decompiling to obfuscation checking) using written rule packs. It also allows the security tester to automatically collect test data (in JSON or CSV) from the code obfuscation checks.  In addition, rule packs can be customized to handle more obfuscation patterns that are unique to the different organizations standards. Future enhancement can include usage in Android malware analysis (where apps are downloaded automatically from Play store and tested).