from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
        <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yangi Vazifa Yaratish</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            font-size: 24px;
        }
        form {
            max-width: 400px;
        }
        label {
            font-weight: bold;
            display: block;
            margin: 10px 0 5px;
        }
        input, textarea, select, button {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Yangi vazifa yaratish</h1>
    <form>
        <label for="task-name">Vazifa nomi:</label>
        <input type="text" id="task-name" name="task-name" placeholder="Vazifa nomini kiriting" required>

        <label for="description">Tavsif:</label>
        <textarea id="description" name="description" rows="4" placeholder="Vazifa tavsifini kiriting"></textarea>

        <label for="deadline">Muddati:</label>
        <input type="date" id="deadline" name="deadline">

        <label for="priority">Muhimlik darajasi:</label>
        <select id="priority" name="priority">
            <option value="low">Past</option>
            <option value="medium">O'rta</option>
            <option value="high">Yuqori</option>
        </select>

        <button type="submit">Vazifani saqlash</button>
    </form>
</body>
</html>

    """
    return HttpResponse(html_response)