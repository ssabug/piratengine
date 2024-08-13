programName="piratengine"
system="linux"
version=0.1.1
buildDir="build"
distDir="dist"
venvDir="venv"
buildZip="y"
deleteBuildFiles="y"
pr="////////////////////////// "

install() {

    if [ -d "${venvDir}" ]; then
        echo "${pr}VENV directory already created, no librairies will be installed"
    else
        echo "${pr}Creating VENV"
        python -m venv venv
        source venv/bin/activate
        echo "${pr}Installing libraries"
        pip install -r utils/requirements.txt        
    fi
}

cleanDirs() {
    rm -rf "${buildDir}/"
    rm -rf "${distDir}/"
}

deleteFiles() {

    if [ "${deleteBuildFiles}" = "y" ]; then
        cleanDirs
    fi

}

prepareBinary() {

    echo "${pr}Creating binary"
    source venv/bin/activate

    python -O -m PyInstaller piratengine.py

    echo "${pr}Installing libraries"

    dataDestDir="${distDir}/${programName}/data"
    mkdir -p "${dataDestDir}"
    cp "data/config.json" "${dataDestDir}/"

    docDestDir="${distDir}/${programName}/doc"
    mkdir -p "${docDestDir}"
    cp -R "doc"/* "${docDestDir}/"
    cp "README.md" "${docDestDir}/"

    mv "${programName}.spec" "${docDestDir}/"

    if [ "${buildZip}" = "y" ]; then
        echo "${pr}Creating ZIP release package"
        cd "${distDir}"
        zip -r "${programName}_${version}_${system}.zip" "${programName}"
        mv "${programName}_${version}_${system}.zip" ../
        cd ..
    fi

    deleteFiles

    echo "${pr}Build terminated, if zip file not created, check errors in terminal"
}

install
cleanDirs
prepareBinary

