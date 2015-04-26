VERSION=$1

if [[ ${VERSION} -eq 3 ]]; then
  PYTHONPATH=/opt/boxen/homebrew/Cellar/python3/3.4.3
elif [[ ${VERSION} -eq 2 ]]; then
  PYTHONPATH=/opt/boxen/homebrew/Cellar/python/2.7.9
else
  echo "VERSION needs to be 2 or 3"
fi

export PATH=${PYTHONPATH}/bin:${PATH}
