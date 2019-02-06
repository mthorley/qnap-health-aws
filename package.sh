#https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/

mkdir pkg

cd pkg

rm -rf *

cp ../src/*.py .

# dependencies
pip3 install xmldict>=0.10.0 -t ./
pip3 install qnapstats -t ./

chmod -R 755 .

zip -r qnapTempLambda.zip .

mv qnapTempLambda.zip ..

