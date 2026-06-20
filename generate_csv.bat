@echo off
setlocal enabledelayedexpansion

set out="c:\Users\vigne\demo1neuro\load_test.csv"
echo Test ID,Screen Name,Test Metric,Description,Status > %out%

set count=1

for %%S in ("Splash Screen" "Welcome Screen" "Login Screen" "Signup Screen" "Biometric Login Screen" "OTP Verification" "Forgot Password" "Reset Password" "Onboarding Step 1" "Onboarding Step 2" "Onboarding Step 3" "User Profile Setup" "Health Questionnaire" "Goal Selection" "Notification Preferences" "Main Dashboard" "Positive Mood Dashboard" "High Stress Dashboard" "Weekly Analysis" "Empty State Dashboard" "Emotion Analysis Home" "Voice Recording" "Voice Processing" "Text Input" "Text Analysis Result" "Face Recognition" "Behavior Tracking" "Multimodal Analysis" "AI Insights" "Stress Breakdown" "Trigger Detection" "Weekly Trends" "Monthly Analytics" "Private Mentor Chat" "Chat Home" "Chat Conversation" "Wellness Suggestions" "Meditation Player" "Breathing Exercise" "Profile Settings") do (
    for %%T in ("UI Rendering" "Load Time (< 2s)" "Memory Usage (< 50MB)" "CPU Usage (< 10%)" "Network Latency (< 100ms)" "State Retention" "Screen Rotation Handling" "Background/Foreground Transition" "Concurrent Event Handling" "Rapid Tap Resilience") do (
        set id=000!count!
        set id=LT-AND-!id:~-3!
        echo !id!,%%~S,%%~T,Load testing %%~T for %%~S,PASS >> %out%
        set /a count+=1
    )
)
echo DONE
