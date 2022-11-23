import org.python.util.PythonInterpreter;
import org.python.core.PyObject;
import org.python.core.PyString;

public class Main
{
    public static void main(String[] args)
    {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("from person import Person");
        PyObject Person = interpreter.get("Person");
        
        PyObject p = Person.__call__(new PyString("Donald"), new PyString("Duck"));
        PersonInterface donald = (PersonInterface)p.__tojava__(PersonInterface.class);
        
        System.out.println(donald.getName());
    }
}