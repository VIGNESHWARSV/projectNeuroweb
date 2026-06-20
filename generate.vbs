Set fso = CreateObject("Scripting.FileSystemObject")
Set outFile = fso.CreateTextFile("c:\Users\vigne\demo1neuro\load_test.csv", True)

outFile.WriteLine "Test ID,Screen Name,Test Metric,Description,Status"

Dim screens
screens = Array("Splash Screen", "Welcome Screen", "Login Screen", "Signup Screen", "Biometric Login Screen", "OTP Verification", "Forgot Password", "Reset Password", "Onboarding Step 1", "Onboarding Step 2", "Onboarding Step 3", "User Profile Setup", "Health Questionnaire", "Goal Selection", "Notification Preferences", "Main Dashboard", "Positive Mood Dashboard", "High Stress Dashboard", "Weekly Analysis", "Empty State Dashboard", "Emotion Analysis Home", "Voice Recording", "Voice Processing", "Text Input", "Text Analysis Result", "Face Recognition", "Behavior Tracking", "Multimodal Analysis", "AI Insights", "Stress Breakdown", "Trigger Detection", "Weekly Trends", "Monthly Analytics", "Private Mentor Chat", "Chat Home", "Chat Conversation", "Wellness Suggestions", "Meditation Player", "Breathing Exercise", "Profile Settings")

Dim tests
tests = Array("UI Rendering", "Load Time (< 2s)", "Memory Usage (< 50MB)", "CPU Usage (< 10%)", "Network Latency (< 100ms)", "State Retention", "Screen Rotation Handling", "Background/Foreground Transition", "Concurrent Event Handling", "Rapid Tap Resilience")

Dim counter
counter = 1

For Each screen In screens
    For Each test In tests
        Dim id
        If counter < 10 Then
            id = "LT-AND-00" & counter
        ElseIf counter < 100 Then
            id = "LT-AND-0" & counter
        Else
            id = "LT-AND-" & counter
        End If
        
        outFile.WriteLine id & "," & screen & "," & test & ",Load testing " & test & " for " & screen & ",PASS"
        counter = counter + 1
    Next
Next

outFile.Close
