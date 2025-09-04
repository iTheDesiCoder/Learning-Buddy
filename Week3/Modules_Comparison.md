# Modules Comparison – COBOL vs Java vs C# vs Python

---

## 🔹 Modules

| Language | How Modules Work | Example |
|----------|------------------|---------|
| **COBOL** | Uses **COPYBOOKS** – code/text inserted at compile-time. | `COPY CUSTOMER-REC.` |
| **Java** | Each `.java` file defines a **class**. Classes are grouped into **packages**. | `package com.company; public class Main {}` |
| **C#** | Code organized in **namespaces**. Compiled into DLL/EXE assemblies. | `namespace MyApp { class Program {} }` |
| **Python** | Any `.py` file is a **module**. Interpreted at runtime. | `import mymodule` |

---

## 🔹 Packages

| Language | Concept | Example |
|----------|---------|---------|
| **COBOL** | No direct concept of package. COPYBOOKs approximate reuse. | `COPY CUSTOMER-REC.` |
| **Java** | Directory structure = package name. Bundled into JAR files. | `package com.company.utils;` |
| **C#** | Uses **namespaces**. Bundled into assemblies (DLL/EXE). | `using System.IO;` |
| **Python** | A folder with `__init__.py` is a **package**. Distributed as wheel on PyPI. | `import mypackage.module` |

---

## 🔹 Import / Use of Code

| Language | Import Mechanism | Example |
|----------|------------------|---------|
| **COBOL** | COPY inserts code directly. | `COPY CUSTOMER-REC.` |
| **Java** | `import` brings in classes from compiled packages. | `import java.util.List;` |
| **C#** | `using` imports namespaces. | `using System.Collections.Generic;` |
| **Python** | `import` executes module at runtime, making functions/classes available. | `from math import sqrt` |

---

## 🔹 Third-Party Libraries

| Language | Ecosystem | Example |
|----------|-----------|---------|
| **COBOL** | Vendor libraries linked during compile or run. | External sort libraries |
| **Java** | Maven/Gradle → pulls JARs. | `mvn install package-name` |
| **C#** | NuGet → manages DLL packages. | `Install-Package Newtonsoft.Json` |
| **Python** | PyPI via `pip`. | `pip install requests` |

---

## 🔹 Execution Model

| Language | Execution | Notes |
|----------|-----------|-------|
| **COBOL** | Compiled into machine code or intermediate p-code. | COPY resolved at compile-time. |
| **Java** | Compiled → bytecode → JVM executes. | Imports resolved at compile-time. |
| **C#** | Compiled → MSIL → CLR executes. | Namespaces resolved at compile-time. |
| **Python** | Interpreted. Import executes the file the first time at runtime. | Dynamic and flexible. |

---

## 🔹 Small Code Examples

### COBOL (COPY)
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.
DATA DIVISION.
WORKING-STORAGE SECTION.
COPY CUSTOMER-REC.

PROCEDURE DIVISION.
    DISPLAY CUSTOMER-NAME.
    STOP RUN.
```

### Java (Package + Import)
```java
package com.company;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello from Java");
    }
}
```

### C# (Namespace + Using)
```csharp
using System;

namespace MyApp {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Hello from C#");
        }
    }
}
```

### Python (Module + Import)
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import mymodule
print(mymodule.greet("Alice"))
```

---

## 💡 Key Takeaways
- COBOL → COPY = compile-time inclusion.  
- Java/C# → Modules & packages compiled first, imported at runtime (bytecode/IL).  
- Python → Any `.py` file is a module; imports are executed dynamically at runtime.  
- Python’s `__init__.py` ≈ package declaration, similar to Java packages / C# namespaces.  

---
