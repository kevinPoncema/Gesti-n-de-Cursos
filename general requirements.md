# 📄 Requerimientos Funcionales

## API REST – Plataforma de Cursos Online

---

## 1. Propósito del Sistema

La API debe permitir **gestionar una plataforma de cursos online** y exponer toda su funcionalidad vía endpoints REST.

El objetivo principal es:

* Implementar reglas de negocio reales
* Validar flujos completos de usuario
* Forzar el uso de ORM avanzado y arquitectura por capas

---

## 2. Comportamiento General de la API

La API debe:

* Responder exclusivamente en JSON
* Validar todas las entradas del cliente
* Retornar códigos HTTP correctos
* Proteger recursos según rol y propiedad

---

## 3. Reglas de Autenticación y Autorización

### 3.1 Autenticación

La API debe:

* Permitir registro de usuarios
* Permitir login mediante JWT
* Requerir token válido para endpoints protegidos

Validaciones:

* Email único
* Password mínimo de 8 caracteres
* No permitir login de usuarios inactivos

---

### 3.2 Autorización

La API debe restringir acciones según rol:

* **Admin**:

  * Acceso total a todos los recursos

* **Instructor**:

  * Crear, editar y eliminar solo sus cursos
  * Publicar cursos
  * Consultar estadísticas propias

* **Student**:

  * Inscribirse en cursos publicados
  * Ver su progreso
  * Crear una sola review por curso

Validaciones:

* Un usuario no puede actuar sobre recursos que no le pertenecen

---

## 4. Requerimientos Funcionales por Entidad

---

### 4.1 Usuarios

La API debe permitir:

* Obtener información del usuario autenticado
* Consultar usuarios (solo admin)

Validaciones:

* No exponer passwords
* No permitir modificar el rol vía API pública

---

### 4.2 Cursos

La API debe permitir:

* Crear cursos (solo instructor)
* Editar cursos propios
* Eliminar cursos propios
* Listar cursos publicados
* Ver detalle de un curso

Validaciones:

* Un curso no publicado no es visible a estudiantes
* Solo el instructor propietario puede modificarlo
* El nivel debe ser uno de: basico, intermedio, avanzado

---

### 4.3 Publicación de Cursos

La API debe permitir:

* Publicar un curso mediante acción explícita

Validaciones:

* Un curso solo puede publicarse una vez
* Solo el instructor propietario puede publicarlo

---

### 4.4 Módulos y Lecciones

La API debe permitir:

* Crear módulos dentro de un curso
* Crear lecciones dentro de un módulo

Validaciones:

* Los módulos deben respetar un orden único por curso
* Las lecciones deben tener duración positiva

---

### 4.5 Inscripciones

La API debe permitir:

* Inscribirse en un curso
* Consultar cursos inscritos del usuario

Validaciones:

* Un usuario no puede inscribirse dos veces al mismo curso
* Solo estudiantes pueden inscribirse
* Solo cursos publicados aceptan inscripciones

---

### 4.6 Progreso

La API debe:

* Calcular progreso automáticamente
* Retornar progreso como porcentaje

Validaciones:

* El progreso debe estar entre 0 y 100

---

### 4.7 Reviews

La API debe permitir:

* Crear una review por curso
* Listar reviews de un curso

Validaciones:

* Rating entre 1 y 5
* Un usuario solo puede dejar una review por curso
* Solo usuarios inscritos pueden dejar reviews

---

## 5. Endpoints Funcionales Obligatorios

### Autenticación

```
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
```

### Cursos

```
GET  /api/courses/
GET  /api/courses/{id}/
POST /api/courses/
PUT  /api/courses/{id}/
```

### Acciones

```
POST /api/courses/{id}/publish/
POST /api/courses/{id}/enroll/
```

### Reviews

```
POST /api/courses/{id}/reviews/
GET  /api/courses/{id}/reviews/
```

---

## 6. Requerimientos de Consultas Avanzadas

La API debe exponer endpoints que:

* Calculen estadísticas agregadas
* Utilicen joins entre múltiples entidades

### Consultas requeridas:

* Cursos más populares
* Ranking de instructores
* Progreso del usuario

---

## 7. Reglas Técnicas Obligatorias

El sistema debe:

* Usar Django ORM sin SQL crudo
* Encapsular queries complejas en repositories
* Encapsular lógica de negocio en services
* Mantener views delgadas

---

## 8. Datos de Prueba

Debe existir un comando:

```
python manage.py seed_data
```

Debe generar:

* Usuarios con distintos roles
* Cursos con módulos y lecciones
* Inscripciones cruzadas
* Reviews coherentes

---

## 9. Criterios de Cumplimiento

El sistema cumple si:

* Todas las validaciones se aplican
* Los permisos funcionan correctamente
* Los endpoints devuelven datos consistentes
* Las consultas son eficientes

---

📌 **Este documento define QUÉ debe hacer la API y QUÉ reglas debe cumplir.**
