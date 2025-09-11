from django.db import models

class Notice(models.Model):
    """공지사항 모델"""
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"
        ordering = ['-created_at']

    def __str__(self):
        return self.title