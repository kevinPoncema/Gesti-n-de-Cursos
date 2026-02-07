# 📄 Requerimientos Generales

## API REST – Plataforma de Cursos Online

---

## 1. Objetivo del Sistema

Desarrollar una **API REST** usando **Django + Django REST Framework** que permita gestionar una plataforma de cursos online.

El sistema debe servir como proyecto de aprendizaje avanzado y cubrir:

* Autenticación y autorización
* Modelado de dominio complejo
* Relaciones entre entidades
* Consultas avanzadas con ORM
* Arquitectura por capas (models / repositories / services)

---

## 2. Alcance

El sistema **NO incluye frontend**. Todo el acceso se realiza vía API REST.

El sistema debe permitir:

* Gestión de usuarios con roles
* Gestión de cursos y contenido educativo
* Inscripciones y progreso
* Reviews y ratings
* Endpoints analíticos y estadísticos

---

## 3. Roles del Sistema

### 3.1 Roles disponibles

* **Admin**: acceso total
* **Instructor**: crea y gestiona cursos propios
* **Student**: se inscribe, progresa y comenta

---

## 4. Entidades del Sistema

### 4.1 User

Entidad base de autenticación.

Campos:

* id
* email (único)
* username
* password
* role (admin | instructor | student)
* is_active
* created_at

---

### 4.2 Instructor

Extensión del usuario.

Relación:

* OneToOne → User

Campos:

* bio
* rating_promedio (calculado)

---

### 4.3 Course

Curso educativo.

Relaciones:

* ManyToOne → Instructor

Campos:

* id
* titulo
* descripcion
* nivel (basico | intermedio | avanzado)
* publicado (bool)
* created_at

---

### 4.4 Module

Agrupa lecciones dentro de un curso.

Relaciones:

* ManyToOne → Course

Campos:

* id
* titulo
* orden

---

### 4.5 Lesson

Contenido individual del curso.

Relaciones:

* ManyToOne → Module

Campos:

* id
* titulo
* duracion_minutos

---

### 4.6 Enrollment

Relación entre usuario y curso.

Relaciones:

* ManyToOne → User
* ManyToOne → Course

Campos:

* id
* progreso (0–100)
* fecha_inscripcion

Restricciones:

* Un usuario solo puede inscribirse una vez por curso

---

### 4.7 Review

Opinión del usuario sobre un curso.

Relaciones:

* ManyToOne → User
* ManyToOne → Course

Campos:

* id
* rating (1–5)
* comentario
* created_at

Restricciones:

* Un usuario solo puede dejar una review por curso

---

## 5. Autenticación y Seguridad

### 5.1 Autenticación

* JWT (access + refresh)
* Registro y login vía API

### 5.2 Autorización

* Permisos por rol
* Permisos por objeto (propietario del recurso)

---

## 6. Endpoints del API

### 6.1 Autenticación

```
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/refresh/
```

---

### 6.2 Usuarios

```
GET    /api/users/me/
GET    /api/users/{id}/        (admin)
```

---

### 6.3 Cursos

```
GET    /api/courses/
GET    /api/courses/{id}/
POST   /api/courses/           (instructor)
PUT    /api/courses/{id}/      (owner)
DELETE /api/courses/{id}/      (owner)
```

---

### 6.4 Acciones sobre cursos

```
POST   /api/courses/{id}/publish/
POST   /api/courses/{id}/enroll/
```

---

### 6.5 Inscripciones

```
GET    /api/enrollments/my/
```

---

### 6.6 Reviews

```
POST   /api/courses/{id}/reviews/
GET    /api/courses/{id}/reviews/
```

---

### 6.7 Estadísticas y consultas complejas

#### Cursos populares

```
GET /api/stats/courses/popular/
```

Devuelve:

* total_inscritos
* rating_promedio
* total_reviews

---

#### Ranking de instructores

```
GET /api/stats/instructors/top/
```

Devuelve:

* total_cursos
* total_alumnos
* rating_promedio

---

#### Progreso del usuario

```
GET /api/stats/my-progress/
```

Devuelve:

* cursos inscritos
* lecciones totales
* progreso

---

## 7. Consultas ORM Requeridas

El sistema debe incluir consultas con:

* annotate
* aggregate
* Count / Avg
* Subquery
* OuterRef
* F expressions
* Q objects

---

## 8. Datos de Prueba (Seed)

Debe existir un comando de carga de datos:

```
python manage.py seed_data
```

Mínimos requeridos:

* 1,000 usuarios
* 20 instructores
* 100 cursos
* 10,000 lecciones
* 5,000 inscripciones
* 8,000 reviews

---

## 9. Requisitos Técnicos

* Python 3.11+
* Django
* Django REST Framework
* JWT Auth
* PostgreSQL (recomendado)
* Arquitectura por capas

---

## 10. Criterios de Éxito

El proyecto se considera exitoso si:

* La API funciona correctamente
* Los permisos se respetan
* Las queries están optimizadas
* El código está organizado por capas
* Existen datos de prueba realistas

---

## 11. Extensiones Futuras (Opcional)

* Cache
* Rate limiting
* Versionado de API
* Tests automatizados
* Documentación OpenAPI

---

📌 **Este documento define el contrato funcional del sistema.**
