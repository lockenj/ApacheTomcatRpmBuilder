ApacheTomcatRpmBuilder
==============

Apache has for some reason decided to neglect the RPM world so this project is targeted to allow people to build RPM packaged versions of Apache's Tomcat.
Gradle is our choice for build tools so with that in mind and thanks to @sharplet for his tomcat init-script, we have a first pass at an rpm builder.

##Usage
1. from the root of the project run "gradle assemble"
2. A tarball can then be found in "build/distributions"
3. The rpm file can be found in "build/RPMS"

##Requirements
1. Java
2. Gradle
3. rpmbuild

##Future Enhancements
- Add auto download of latest tomcat
- Add runline arg support for different versions of tomcat
