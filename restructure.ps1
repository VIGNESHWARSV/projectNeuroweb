New-Item -ItemType Directory -Force -Path "c:\Users\vigne\demo1neuro\android_project" | Out-Null
New-Item -ItemType Directory -Force -Path "c:\Users\vigne\demo1neuro\web_project" | Out-Null

Write-Output "Moving android contents..."
Move-Item -Path "c:\Users\vigne\demo1neuro\android\*" -Destination "c:\Users\vigne\demo1neuro\android_project" -Force -ErrorAction Continue

Write-Output "Moving frontend contents..."
Move-Item -Path "c:\Users\vigne\demo1neuro\frontend\*" -Destination "c:\Users\vigne\demo1neuro\web_project" -Force -ErrorAction Continue

Write-Output "Moving other folders..."
$folders = @("backend", "selenium-tests", ".firebase")
foreach ($f in $folders) {
    if (Test-Path "c:\Users\vigne\demo1neuro\$f") {
        Move-Item -Path "c:\Users\vigne\demo1neuro\$f" -Destination "c:\Users\vigne\demo1neuro\web_project\$f" -Force -ErrorAction Continue
    }
}

Write-Output "Moving individual files..."
$files = @(".firebaseignore", ".firebaserc", "firebase.json", "firestore.rules", "local-auth.js")
foreach ($f in $files) {
    if (Test-Path "c:\Users\vigne\demo1neuro\$f") {
        Move-Item -Path "c:\Users\vigne\demo1neuro\$f" -Destination "c:\Users\vigne\demo1neuro\web_project\$f" -Force -ErrorAction Continue
    }
}

Write-Output "Moving python scripts..."
Get-ChildItem -Path "c:\Users\vigne\demo1neuro\*.py" | Where-Object { $_.Name -ne "restructure.py" } | Move-Item -Destination "c:\Users\vigne\demo1neuro\web_project\" -Force -ErrorAction Continue

Write-Output "Done."
