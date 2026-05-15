using System;
using System.Diagnostics;
using System.IO;
using System.Text;

internal static class UpdateArmorDbAndBuild
{
    private static int Main(string[] args)
    {
        string exeDir = AppDomain.CurrentDomain.BaseDirectory;
        string scriptPath = Path.Combine(exeDir, "update-armor-db-and-build.ps1");

        if (!File.Exists(scriptPath))
        {
            Console.Error.WriteLine("Script not found: " + scriptPath);
            Console.Error.WriteLine("Keep update-armor-db-and-build.exe in the tools folder.");
            Console.WriteLine();
            Console.Write("Press Enter to exit...");
            Console.ReadLine();
            return 2;
        }

        string windowsDir = Environment.GetFolderPath(Environment.SpecialFolder.Windows);
        string powershell = Path.Combine(windowsDir, @"System32\WindowsPowerShell\v1.0\powershell.exe");
        if (!File.Exists(powershell))
        {
            powershell = "powershell.exe";
        }

        string arguments = "-NoProfile -ExecutionPolicy Bypass -File " + Quote(scriptPath);
        foreach (string arg in args)
        {
            arguments += " " + Quote(arg);
        }

        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = powershell,
            Arguments = arguments,
            UseShellExecute = false
        };

        using (Process process = Process.Start(startInfo))
        {
            process.WaitForExit();
            return process.ExitCode;
        }
    }

    private static string Quote(string value)
    {
        if (value == null)
        {
            return "\"\"";
        }

        StringBuilder builder = new StringBuilder();
        builder.Append('"');
        int backslashes = 0;
        foreach (char ch in value)
        {
            if (ch == '\\')
            {
                backslashes += 1;
                continue;
            }

            if (ch == '"')
            {
                builder.Append('\\', backslashes * 2 + 1);
                builder.Append('"');
                backslashes = 0;
                continue;
            }

            if (backslashes > 0)
            {
                builder.Append('\\', backslashes);
                backslashes = 0;
            }
            builder.Append(ch);
        }

        if (backslashes > 0)
        {
            builder.Append('\\', backslashes * 2);
        }
        builder.Append('"');
        return builder.ToString();
    }
}
