from zope.publisher.browser import BrowserView

def getStudents(context):
    result = context.portal_catalog.searchResults(
          portal_type='Student',
          path='/'.join(context.getPhysicalPath()),
          sort_on='created',
          sort_order='reverse'
        )
    return result

class StudentList(BrowserView):
    """
    student list
    """
    def getStudents(self):
        result = getStudents(self.context)
        return result


class StudentPortfolios(StudentList):
    """
    student portfolios
    """