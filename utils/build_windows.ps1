@ECHO OFF

$programName=piratengine
$system="windows"
$version=0.1.1
$buildDir="build"
$distDir="dist"
$venvDir="venv"
$buildZip="y"
$deleteBuildFiles="y"
$pr="////////////////////////// "
echo "${pr} ensure python has the permission to run scripts, by running in an admin powershell window : Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"

function install {
    if exist $venvDir (
    echo "${pr}VENV directory already created, no librairies will be installed"
    ) else (
    echo "${pr}Creating VENV"
        python -m venv venv
        .\venv\Scripts\Activate.ps1 
        echo "${pr}Installing libraries"
        pip install -r utils\requirements.txt       
    )
}

function cleanDirs {
    Remove-Item "$buildDir"
    Remove-Item "$distDir"
}

function deleteFiles {
    if "${deleteBuildFiles}"=="y" (
        cleanDirs
    )
}

function prepareBinary {
    echo "${pr}Creating binary"
    .\venv\Scripts\Activate.ps1
    python -O -m PyInstaller piratengine.py
    echo "${pr}Copying program data"

    $dataDestDir="${distDir}\${programName}\data"
    New-Item -Name "${dataDestDir}" -ItemType "directory"
    Copy-Item -Path "data/config.json" -Destination "${dataDestDir}"

    $docDestDir="${distDir}\${programName}\doc"
    New-Item -Name "${docDestDir}" -ItemType "directory"
    Copy-Item -Path "doc\*" -Destination "${docDestDir}" -Recurse
    Copy-Item -Path "README.md" -Destination "${docDestDir}"
    Move-Item -Path "${programName}.spec" -Destination "${docDestDir}\${programName}.spec"

    if "${buildZip}"=="y" (
        $zipfile="${programName}_${version}_${system}.zip"
        echo "${pr}Creating ZIP release package ${zipfile}"
        cd "${distDir}"
        $compress = @{
            Path = "${distDi}\${programName}"
            CompressionLevel = "Fastest"
            DestinationPath = "${zipfile}"
        }
        Compress-Archive @compress
        Move-Item -Path "${zipfile}" -Destination "${docDestDir}\${zipfile}"
        cd ..
    )
    deleteFiles
}

install
cleanDirs
prepareBinary