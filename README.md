# hello-onefactor
Test for OneFactor

All steps are tested on Centos 7 x64


# To build jar:
```
sudo yum install git maven rpm-build -y
```
make java7 as a default:
```
sudo alternatives --config java
```
```
git clone https://github.com/meshok0/hello-onefactor.git
cd hello-onefactor/
mvn package
```

# To build rpm:
```
cd ~
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,tmp}
cd rpmbuild
mkdir -p hello-onefactor-0.0.3/{usr/lib,etc/systemd/system}
cp ../hello-onefactor/target/hello-onefactor-0.0.3.jar hello-onefactor-0.0.3/usr/lib/
cp ../hello-onefactor/hello-onefactor.service hello-onefactor-0.0.3/etc/systemd/system/


```


