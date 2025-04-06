
// 구조체 정의
struct Student {
    int id;
    char name[20];
    float score;
    struct Student* next; // 다음 학생을 가리키는 포인터
};


struct  School {
    int school_num;
    char* school_name;
    int 개교년도;
};
