using IronPython.Hosting;

class Beispiel
{
    static void Main(string[] args)
    {
        var engine = Python.CreateEngine();
        var scope = engine.CreateScope();
        engine.ExecuteFile("script.py", scope);
        
        System.Console.Write(engine.Operations.Invoke(scope.GetVariable("quadrat"), 5));
    }
}