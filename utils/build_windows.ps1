
$programName="piratengine"
$system="windows"
$workingDir="$(Get-Location)"
$version="0.1.2"
$buildDir="${workingDir}\build"
$distDir="${workingDir}\dist"
$venvDir="${workingDir}\venv"
$buildZip="y"
$deleteBuildFiles="y"
$pr="////////////////////////// "

echo "${pr}Troubleshooting :"
echo "  - ensure git command is available on the system in powershell terminal "
echo "  - ensure python command is availabe in powershell - prefer Microsoft store install for this"
echo "  - ensure python has the permission to run scripts, by running in an admin powershell window : Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
echo " "

echo "${pr}Working dir $(Get-Location)"

function patch {
    echo "Patching announce IP in PyStageLinQ 0.1.2"  
    $file = Get-ChildItem venv\lib -Recurse -Include PyStageLinQ.py
    $regex = '169.254.255.255'
    (Get-Content $file) -replace $regex, '224.0.0.251' | Set-Content $file
}

function install {
    if (Test-Path -Path "$venvDir") {
    echo "${pr}VENV directory already created, no librairies will be installed"
    } else {
        echo "${pr}Creating VENV"
        python -m venv venv
        echo "${pr}Activating VENV"
        .\venv\Scripts\Activate.ps1 
        echo "${pr}Installing libraries"
        pip install -r utils\requirements.txt    
        #use the line below if PyStageLinQ version is 0.1.2
        #patch
    }
}

function cleanDirs {
    Remove-Item "$buildDir" -Recurse -Force
    Remove-Item "$distDir"	-Recurse -Force
}

function deleteFiles {
    if ("${deleteBuildFiles}" -eq "y") {
        cleanDirs
    }
}

function prepareBinary {
    echo "${pr}Creating binary"
    .\venv\Scripts\Activate.ps1
    python -O -m PyInstaller piratengine.py
    echo "${pr}Copying program data"

    $dataDestDir="${distDir}\${programName}\data"
    New-Item -Path "${dataDestDir}" -ItemType "directory"
    Copy-Item -Path "data/config.json" -Destination "${dataDestDir}"

    $docDestDir="${distDir}\${programName}\doc"
    New-Item -Path "${docDestDir}" -ItemType "directory"
    Copy-Item -Path "doc\*" -Destination "${docDestDir}" -Recurse
    Copy-Item -Path "README.md" -Destination "${docDestDir}"
    Move-Item -Path "${programName}.spec" -Destination "${docDestDir}\${programName}.spec"

    if ("${buildZip}" -eq "y") {
        $zipfile="${programName}_${version}_${system}.zip"
        echo "${pr}Creating ZIP release package ${zipfile}"
        cd "${distDir}"
        $compress = @{
            Path = "${distDir}\${programName}"
            CompressionLevel = "Fastest"
            DestinationPath = "${workingDir}\${zipfile}"
        }
        Compress-Archive @compress
        cd ..
    }
    #deleteFiles
	
	echo "${pr}Build terminated, if zip file not created, check errors in terminal"
}

install
cleanDirs
prepareBinary