## 3. TypeError

**Error:** `TypeError: can only concatenate str (not "int") to str`

**Cause:** Incompatible data types ko ek operation me use karne par TypeError aata hai.

**Code that triggers the error:**
```python
age = "20"
print(age + 5)