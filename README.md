Перед запуском, задайте значения для переменных VK_TOKEN  и VK_GROUP (короткое имя группы на английском)  в "backend/djangovue/settings.py"  
Как запустить приложение в dev режиме:  
Запустите дев сервера django и node в разных терминалах (например используя tmux):  
cd backend/  
./manage runserver  
Во втором терминале:  
cd frontend/  
npm run dev  

После зайдите по адресу сгенерированному в node dev server (обычно это http://localhost:8080)  
