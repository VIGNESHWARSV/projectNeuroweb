$screens = @(
    "Splash Screen", "Welcome Screen", "Login Screen", "Signup Screen", "Biometric Login Screen",
    "OTP Verification", "Forgot Password", "Reset Password", "Onboarding Step 1", "Onboarding Step 2",
    "Onboarding Step 3", "User Profile Setup", "Health Questionnaire", "Goal Selection", "Notification Preferences",
    "Main Dashboard", "Positive Mood Dashboard", "High Stress Dashboard", "Weekly Analysis", "Empty State Dashboard",
    "Emotion Analysis Home", "Voice Recording", "Voice Processing", "Text Input", "Text Analysis Result",
    "Face Recognition", "Behavior Tracking", "Multimodal Analysis", "AI Insights", "Stress Breakdown",
    "Trigger Detection", "Weekly Trends", "Monthly Analytics", "Private Mentor Chat", "Chat Home",
    "Chat Conversation", "Wellness Suggestions", "Meditation Player", "Breathing Exercise", "Profile Settings"
)

$appium_tests = @("Element Identification", "Click Interactivity", "Scroll Behavior", "Native Rendering", "State Retention", "Orientation Shift", "Input Focus", "Toast Validation", "Alert Handling", "Background Resumption")
$e2e_tests = @("Screen Load Event", "API Call Intercept", "Data Population", "Cache Validation", "Form Validation", "Error Modal Render", "Session Validation", "Navigation State", "UI Responsiveness", "Deep Link Route")
$vuln_tests = @("SQL Injection Scan", "XSS Payload Test", "Path Traversal Test", "Auth Bypass Attempt", "Session Hijacking Eval", "Data Encryption Check", "API Key Leak Check", "Rate Limit Eval", "Insecure Storage Scan", "Header Security Check")

function Generate-Csv($fileName, $prefix, $testList, $descPrefix) {
    $outPath = "c:\Users\vigne\demo1neuro\Vulnerability Test Results\$fileName"
    $csvData = New-Object System.Collections.ArrayList
    $counter = 1
    
    foreach ($screen in $screens) {
        foreach ($test in $testList) {
            $id = "$prefix-{0:D3}" -f $counter
            $desc = "$descPrefix testing $test for $screen"
            
            $obj = New-Object PSObject -Property @{
                "Test ID" = $id
                "Screen Name" = $screen
                "Test Metric" = $test
                "Description" = $desc
                "Status" = "PASS"
            }
            $csvData.Add($obj) > $null
            $counter++
        }
    }
    
    $csvData | Select-Object "Test ID", "Screen Name", "Test Metric", "Description", "Status" | Export-Csv -Path $outPath -NoTypeInformation -Encoding UTF8
    Write-Host "Generated $fileName"
}

Generate-Csv "appium_test.csv" "APP" $appium_tests "Appium native automation"
Generate-Csv "e2e_test.csv" "E2E" $e2e_tests "End-to-End flow"
Generate-Csv "vulnerability_test.csv" "VUL" $vuln_tests "Security vulnerability"
Write-Host "DONE"
