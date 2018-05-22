import compiler.lexer
import compiler.semantic
from ply import lex, yacc
from compiler.lexer import tokens

lex.lex(module=compiler.lexer)
a = '''
#import "aaa.h"
@interface NetworkRequest()
{
    NSURLConnection* urlConnection;
    NSMutableData* urlResponseData;
    NSString *desiredDownloadFilename;
    NSOutputStream* downloadFileStream;
    NSInteger tries;
    NSInteger fileLength;
    NSInteger expectedLength;
    NetworkRequest *selfReference;      // while the response is being delivered, to make sure this object does not die in the middle
    BOOL networkIndicatorStarted;
    BOOL backgroundNotificationForDictionary;
    BOOL hasSentProgressForUpload;
    BOOL uploadRequest;
    BOOL backgroundProcessing;
    NSDictionary<NSString*,id> *parametersForOAuth;
    OAuthToken *oAuthConsumer;
    OAuthToken *oAuthToken;
    NSMutableURLRequest *urlRequest;
    NetworkRequestResponseType responseType;
    NSString *uploadTempFilename;
    double startTime;
}
@property(nonatomic,copy) NetworkRequestDictionaryResponse dictionaryHandler;
@property(nonatomic,copy) NetworkRequestStringResponse stringHandler;
@property(nonatomic,copy) NetworkRequestDataResponse dataHandler;
@property(nonatomic,copy) NetworkRequestFileResponse fileHandler;
@property(nonatomic,copy) NetworkRequestFailedParse failedParseHandler;
@end
'''
# print(a)
lex.input(a)
parser = yacc.yacc(module=compiler.semantic, start=compiler.semantic.start)
# result = parser.parse(a)

while 1:
    tok = lex.token()
    if not tok: break
    print tok

